# PORTS
1. docker-compose-crypto.yaml

    No ports are explicitly mapped in this file.

2. docker-compose-downloaders.yaml

    gluetun:

        6000:9000/tcp

        6881:6881 (TCP and UDP for qBittorrent)

        7000:8000/tcp

        8112:8112 (Deluge)

        8080:8080 (SABnzbd)

        8091:8091 (qBittorrent)

        9091:9091 (Transmission)

        51413:51413 (TCP and UDP for Transmission)

    sabnzbd-exporter:

        9711:9711

    unpackerr:

        5656:5656

3. docker-compose-homeassistant.yaml

    homeassistant:

        Uses network_mode: host, so it binds directly to the host's network interfaces. No specific ports are listed in the file, but Home Assistant typically uses:

            8123 (Web UI)

            Other ports depending on integrations (e.g., Z-Wave, Zigbee).

4. docker-compose-kometa.yaml

    No ports are explicitly mapped in this file.

5. docker-compose-media-players.yaml

    plex:

        3005:3005

        8324:8324

        32400:32400

        32410:32410

        32412:32412

        32413:32413

        32414:32414

        32469:32469

6. docker-compose-ops.yaml

    alertmanager:

        9093:9093

    grafana:

        3000:3000

    iperf3:

        5201:5201

    prometheus:

        9090:9090

    redis:

        6379:6379

    watchtower:

        8484:8080

7. docker-compose-photos.yaml

    immich_server:

        2283:3001

    photoprism:

        2342:2342

8. docker-compose-servarr.yaml

    bazarr:

        6767:6767

    bazarr-exporter:

        9712:9712

    lidarr:

        8686:8686

    lidarr-exporter:

        9709:9709

    mylar3:

        8090:8090

    notifiarr:

        5454:5454

    prowlarr:

        9696:9696

    prowlarr-exporter:

        9710:9710

    radarr:

        7878:7878

    radarr-exporter:

        9708:9708

    readarr:

        8787:8787

    readarr-exporter:

        9713:9713

    sonarr:

        8989:8989

    sonarr-exporter:

        9707:9707

9. docker-compose-tools.yaml

    paperless-ngx:

        8001:8000

    syncthing:

        Uses network_mode: host, so it binds directly to the host's network interfaces. No specific ports are listed in the file, but Syncthing typically uses:

            8384 (Web UI)

            22000 (Sync protocol)

            21027 (Discovery)

Summary of Ports by Service

Service	Ports
gluetun	6000, 6881 (TCP/UDP), 7000, 8112, 8080, 8091, 9091, 51413 (TCP/UDP)
sabnzbd-exporter	9711
unpackerr	5656
plex	3005, 8324, 32400, 32410, 32412, 32413, 32414, 32469
homeassistant	Host mode (typically 8123 and others depending on integrations)
alertmanager	9093
grafana	3000
iperf3	5201
prometheus	9090
redis	6379
watchtower	8484
immich_server	2283
photoprism	2342
bazarr	6767
bazarr-exporter	9712
lidarr	8686
lidarr-exporter	9709
mylar3	8090
notifiarr	5454
prowlarr	9696
prowlarr-exporter	9710
radarr	7878
radarr-exporter	9708
readarr	8787
readarr-exporter	9713
sonarr	8989
sonarr-exporter	9707
paperless-ngx	8001
syncthing	Host mode (typically 8384, 22000, 21027)


