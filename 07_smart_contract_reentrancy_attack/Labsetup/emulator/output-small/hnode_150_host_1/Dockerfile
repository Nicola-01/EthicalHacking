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
COPY f67ad975c1365d5bc76027504b142952 /tmp/keystore/UTC--2023-03-02T12-48-33.239012000Z--0x1081c645CC8c21EfbB0114eAc5fcDBE01a1a4b19
COPY b5e45a0b15e6313235445f52c23845cd /tmp/keystore/UTC--2023-03-02T12-48-43.118944000Z--0xa6bBf9891a0689Fe91d9c1538478b95effe0a57A
COPY d2cdff8371aa6af79bb63954a87ac69f /tmp/eth-password
COPY 0bf749f51915d190035e14f6afa9a371 /tmp/eth-nodes
COPY 427fecb1e0b6c8dc8f669b5b71b8db71 /tmp/eth-bootstrapper
CMD ["/start.sh"]

