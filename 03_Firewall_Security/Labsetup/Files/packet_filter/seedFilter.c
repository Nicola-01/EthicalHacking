#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/udp.h>
#include <linux/if_ether.h>
#include <linux/inet.h>

static struct nf_hook_ops hook1, hook_ping;

unsigned int blockPING(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{

   struct iphdr *iph;
   struct udphdr *udph;

   u16 port = 53;
   char ip[16] = "8.8.8.8";
   u32 ip_addr;

   if (!skb)
      return NF_ACCEPT;

   iph = ip_hdr(skb);
   // Convert the IPv4 address from dotted decimal to 32-bit binary
   in4_pton(ip, -1, (u8 *)&ip_addr, '\0', NULL);

   if (iph->protocol == IPPROTO_UDP)
   {
      udph = udp_hdr(skb);
      if (iph->daddr == ip_addr && ntohs(udph->dest) == port)
      {
         printk(KERN_WARNING "*** Dropping %pI4 (UDP), port %d\n", &(iph->daddr), port);
         return NF_DROP;
      }
   }
   return NF_ACCEPT;
}

unsigned int printInfo(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{
   struct iphdr *iph;
   char *hook;
   char *protocol;

   switch (state->hook)
   {
   case NF_INET_LOCAL_IN: // Hook for packets destined for local processes
      hook = "LOCAL_IN";
      break;

   case NF_INET_LOCAL_OUT: // Hook for packets originating from local processes
      hook = "LOCAL_OUT";
      break;

   case NF_INET_PRE_ROUTING: // Hook for packets before routing decision
      hook = "PRE_ROUTING";
      break;

   case NF_INET_POST_ROUTING: // Hook for packets after routing decision
      hook = "POST_ROUTING";
      break;

   case NF_INET_FORWARD: // Hook for packets being forwarded between interfaces
      hook = "FORWARD";
      break;

   default: // In case of an invalid hook value
      hook = "IMPOSSIBLE";
      break;
   }



   printk(KERN_INFO "*** %s\n", hook); // Print out the hook info

   iph = ip_hdr(skb);
   switch (iph->protocol)
   {
   case IPPROTO_UDP:
      protocol = "UDP";
      break;
   case IPPROTO_TCP:
      protocol = "TCP";
      break;
   case IPPROTO_ICMP:
      protocol = "ICMP";
      break;
   default:
      protocol = "OTHER";
      break;
   }
   // Print out the IP addresses and protocol
   printk(KERN_INFO "    %pI4  --> %pI4 (%s)\n",
          &(iph->saddr), &(iph->daddr), protocol);

   return NF_ACCEPT;
}

int registerFilter(void)
{
   printk(KERN_INFO "Registering filters.\n");

   hook1.hook = printInfo;

   // Ogni hook e\' per un punto specifico della rete, quindi
   // e\' necessario registrare un hook per ciascun punto
   // (pre-routing, post-routing, local-in, local-out, forward).
   hook1.hooknum = NF_INET_LOCAL_OUT;

   hook1.pf = PF_INET; // packet family: PF_INET -> IPv4
   hook1.priority = NF_IP_PRI_FIRST;
   nf_register_net_hook(&init_net, &hook1);

   hook_ping.hook = blockPING;
   hook_ping.hooknum = NF_INET_POST_ROUTING;
   hook_ping.pf = PF_INET;
   hook_ping.priority = NF_IP_PRI_FIRST;
   nf_register_net_hook(&init_net, &hook_ping);

   return 0;
}

void removeFilter(void)
{
   printk(KERN_INFO "The filters are being removed.\n");
   nf_unregister_net_hook(&init_net, &hook1);
   nf_unregister_net_hook(&init_net, &hook_ping);
}

module_init(registerFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");
