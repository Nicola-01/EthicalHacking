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
COPY d9fda1f1d7896b244e58c517c8739f4b /tmp/keystore/UTC--2023-03-02T12-48-32.280145000Z--0x1be9288F9a7D2F809250f15c487E3a5A9Cf71f4F
COPY 437f8fb052fb0127f82822a8c87e5cd7 /tmp/keystore/UTC--2023-03-02T12-48-41.315228000Z--0xA403f63AD02a557D5DDCBD5F5af9A7627C591034
COPY 83b7f303f39ea5273bde4713dd5aa79b /tmp/keystore/UTC--2023-03-02T12-48-42.209410000Z--0x7218bd3E25b42Fb6897FBE7fD16c911331b2096a
COPY d2cdff8371aa6af79bb63954a87ac69f /tmp/eth-password
COPY 0bf749f51915d190035e14f6afa9a371 /tmp/eth-nodes
COPY 427fecb1e0b6c8dc8f669b5b71b8db71 /tmp/eth-bootstrapper
CMD ["/start.sh"]

