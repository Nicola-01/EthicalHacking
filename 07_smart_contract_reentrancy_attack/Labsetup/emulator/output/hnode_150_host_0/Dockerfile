FROM f1d53a66de3c35d8a921558f3b4bdbbd
ARG DEBIAN_FRONTEND=noninteractive
RUN echo 'exec zsh' > /root/.bashrc
RUN apt-get update && apt-get install -y --no-install-recommends curl dnsutils ipcalc iproute2 iputils-ping jq mtr-tiny nano netcat software-properties-common tcpdump termshark vim-nox zsh
RUN curl -L https://grml.org/zsh/zshrc > /root/.zshrc
COPY 082b96ec819c95ae773daebde675ef80 /start.sh
COPY d18858afc6bb66ec3a19d872077acfd2 /seedemu_sniffer
COPY 17ac2d812a99a91e7f747e1defb72a29 /seedemu_worker
RUN chmod +x /start.sh
RUN chmod +x /seedemu_sniffer
RUN chmod +x /seedemu_worker
COPY e01e36443f9f72c6204189260d0bd276 /ifinfo.txt
COPY d3d51fdf7f4bad30dc5db560a01ce629 /interface_setup
COPY f4d556a844298d3911e6d250e4a2d93b /tmp/eth-genesis.json
COPY 47380eb50f3559db922dc6aacd9e2901 /tmp/keystore/UTC--2023-03-02T12-56-14.571721000Z--0x1be9288F9a7D2F809250f15c487E3a5A9Cf71f4F
COPY ccd45833dc8ca4cc25c96334d6d704c4 /tmp/keystore/UTC--2023-03-02T12-56-41.477258000Z--0xA403f63AD02a557D5DDCBD5F5af9A7627C591034
COPY 98788fac9bd8e485c0c6c96fe6ad1144 /tmp/keystore/UTC--2023-03-02T12-56-42.381524000Z--0x7218bd3E25b42Fb6897FBE7fD16c911331b2096a
COPY d2cdff8371aa6af79bb63954a87ac69f /tmp/eth-password
COPY 0bf749f51915d190035e14f6afa9a371 /tmp/eth-nodes
COPY 427fecb1e0b6c8dc8f669b5b71b8db71 /tmp/eth-bootstrapper
CMD ["/start.sh"]

