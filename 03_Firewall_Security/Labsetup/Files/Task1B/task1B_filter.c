#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/udp.h>
#include <linux/if_ether.h>
#include <linux/inet.h>

static struct nf_hook_ops hook1, hook_ping, hook_telnet;

unsigned int printInfo(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{
    struct iphdr *iph;
    struct tcphdr *tcph;
    struct udphdr *udph;
    char *hook;
    char *protocol;
    u16 src_port = 0;
    u16 dest_port = 0;

    switch (state->hook)
    {
    case NF_INET_LOCAL_IN:
        hook = "LOCAL_IN";
        break;
    case NF_INET_LOCAL_OUT:
        hook = "LOCAL_OUT";
        break;
    case NF_INET_PRE_ROUTING:
        hook = "PRE_ROUTING";
        break;
    case NF_INET_POST_ROUTING:
        hook = "POST_ROUTING";
        break;
    case NF_INET_FORWARD:
        hook = "FORWARD";
        break;
    default:
        hook = "IMPOSSIBLE";
        break;
    }
    printk(KERN_INFO "*** %s\n", hook); // Print out the hook info

    iph = ip_hdr(skb);
    if (!iph)
    {
        printk(KERN_WARNING "No IP header\n");
        return NF_ACCEPT; // Handle case where IP header is not present
    }

    switch (iph->protocol)
    {
    case IPPROTO_UDP:
        protocol = "UDP";
        udph = udp_hdr(skb); // Get UDP header
        if (udph)
        {
            src_port = ntohs(udph->source);
            dest_port = ntohs(udph->dest);
        }
        break;
    case IPPROTO_TCP:
        protocol = "TCP";
        tcph = tcp_hdr(skb); // Get TCP header
        if (tcph)
        {
            src_port = ntohs(tcph->source);
            dest_port = ntohs(tcph->dest);
        }
        break;
    case IPPROTO_ICMP:
        protocol = "ICMP";
        break;
    default:
        protocol = "OTHER";
        break;
    }

    // Print out the IP addresses and protocol along with ports if applicable
    printk(KERN_INFO "    %pI4:%u  --> %pI4:%u (%s)\n",
           &(iph->saddr), src_port, &(iph->daddr), dest_port, protocol);

    return NF_ACCEPT;
}

unsigned int blockPING(void *priv, struct sk_buff *skb,
                       const struct nf_hook_state *state)
{
    struct iphdr *iph;

    if (!skb) // null checker
        return NF_ACCEPT;

    iph = ip_hdr(skb);
    if (iph->protocol == IPPROTO_ICMP)
    {
        printk(KERN_WARNING "*** Dropping %pI4 (ICMP), %d\n", &(iph->daddr));
        return NF_DROP;
    }
    return NF_ACCEPT;
}

unsigned int blockTELNET(void *priv, struct sk_buff *skb,
                         const struct nf_hook_state *state)
{
    struct iphdr *iph;
    struct tcphdr *tcph;

    u16 port = 23;

    if (!skb)
        return NF_ACCEPT;

    iph = ip_hdr(skb);
    if (!iph || iph->protocol != IPPROTO_TCP)
        return NF_ACCEPT;

    tcph = tcp_hdr(skb);
    if (!tcph)
        return NF_ACCEPT;

    printk(KERN_WARNING "---------- Destination Port: %u\n", ntohs(tcph->dest));
    printInfo(priv, skb, state);
    if (ntohs(tcph->dest) == port)
    {
        printk(KERN_WARNING "*** Dropping %pI4 (TCP), port %d\n", &(iph->daddr), port);
        return NF_DROP;
    }

    return NF_ACCEPT;
}

int registerFilter(void)
{
    printk(KERN_INFO "Registering filters.\n");

    // hook1.hook = printInfo;
    // hook1.hooknum = NF_INET_LOCAL_IN;
    // hook1.pf = PF_INET;
    // hook1.priority = NF_IP_PRI_FIRST;
    // nf_register_net_hook(&init_net, &hook1);

    hook_ping.hook = blockPING;
    hook_ping.hooknum = NF_INET_PRE_ROUTING;
    hook_ping.pf = PF_INET;
    hook_ping.priority = NF_IP_PRI_FIRST;
    nf_register_net_hook(&init_net, &hook_ping);

    hook_telnet.hook = blockTELNET;
    hook_telnet.hooknum = NF_INET_PRE_ROUTING;
    hook_telnet.pf = PF_INET;
    hook_telnet.priority = NF_IP_PRI_FIRST;
    nf_register_net_hook(&init_net, &hook_telnet);

    return 0;
}

void removeFilter(void)
{
    printk(KERN_INFO "The filters are being removed.\n");
    nf_unregister_net_hook(&init_net, &hook_ping);
    nf_unregister_net_hook(&init_net, &hook_telnet);
}

module_init(registerFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");
