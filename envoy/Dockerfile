FROM envoyproxy/envoy:latest
RUN apt update
COPY envoy.yaml /etc/envoy.yaml
CMD /usr/local/bin/envoy -c /etc/envoy.yaml
