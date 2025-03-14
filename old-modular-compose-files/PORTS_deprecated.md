0- docker-compose-portainer.yaml
 
   portainer:

     - 8888:8888
     - 9999:9999
     - 9443:9443
   



1. docker-compose-crypto.yaml

    No ports are explicitly mapped in this file.

2. docker-compose-downloaders.yaml
Active Services:

    gluetun:

        6000:9000/tcp

        6881:6881 (TCP and UDP)

        7000:8000/tcp

        8112:8112

        8080:8080

        8091:8091

        9091:9091

        51413:51413 (TCP and UDP)

    sabnzbd-exporter:

        9711:9711

    unpackerr:

        5656:5656

Commented Services:

    deluge:

        8112:8112

        58846:58846

        58946:58946/udp

    delugevpn:

        8112:8112

        8118:8118

        58846:58846

        58946:58946/udp

    nzbget:

        6789:6789

    nzbgetvpn:

        6789:6789

    sabnzbdvpn:

        8080:8080

        8090:8090

        8119:8118

        9091:9091

        51413:51413 (TCP and UDP)

    transmission:

        9091:9091

        51413:51413 (TCP and UDP)

    transmission-openvpn:

        8112:8112

        6881:6881 (TCP and UDP)

        9910:9910

        6789:6789

        8080:8080

        9091:9091

3. docker-compose-homeassistant.yaml

    homeassistant:

        Uses network_mode: host, so it binds directly to the host's network interfaces. Typically uses port 8123 for the web UI.

4. docker-compose-kometa.yaml

    No ports are explicitly mapped in this file.

5. docker-compose-media-players.yaml
Active Services:

    plex:

        3005:3005

        8324:8324

        32400:32400

        32410:32410

        32412:32412

        32413:32413

        32414:32414

        32469:32469

Commented Services:

    emby:

        8097:8096

        8921:8920

    jellyfin:

        7359:7359/udp

        8096:8096

        8920:8920

    jellyseerr:

        5056:5055

    overseerr:

        5055:5055

    tautulli:

        8181:8181

6. docker-compose-ops.yaml
Active Services:

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

Commented Services:

    prometheus (commented section):

        9090:9090

7. docker-compose-photos.yaml
Active Services:

    immich_server:

        2283:3001

    photoprism:

        2342:2342

8. docker-compose-servarr.yaml
Active Services:

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
Active Services:

    paperless-ngx:

        8001:8000

    syncthing:

        Host mode (typically 8384, 22000, 21027)

Commented Services:

    searxng:

        8082:8080

    wallabag:

        8092:80

    wallabag_db:

        No ports explicitly mapped.

    wallabag_redis:

        No ports explicitly mapped.

Summary of All Ports (Including Commented Services)

Here’s a consolidated list of all ports used in the docker-compose files, including commented services:
Service	Ports
gluetun	6000, 6881 (TCP/UDP), 7000, 8112, 8080, 8091, 9091, 51413 (TCP/UDP)
sabnzbd-exporter	9711
unpackerr	5656
deluge	8112, 58846, 58946 (UDP)
qbit 8113, 58847, 58947
delugevpn	8112, 8118, 58846, 58946 (UDP)
nzbget	6789
nzbgetvpn	6789
sabnzbdvpn	8080, 8090, 8119, 9091, 51413 (TCP/UDP)
transmission	9091, 51413 (TCP/UDP)
transmission-openvpn	8112, 6881 (TCP/UDP), 9910, 6789, 8080, 9091
homeassistant	Host mode (typically 8123)
plex	3005, 8324, 32400, 32410, 32412, 32413, 32414, 32469
emby	8097, 8921
jellyfin	7359 (UDP), 8096, 8920
jellyseerr	5056
overseerr	5055
tautulli	8181
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
searxng	8082
wallabag	8092
portainer 8888,9999,9443



Conflict Analysis

Now that we’ve included the commented services, let’s check for port conflicts:

    Port 8112:

        Used by gluetun, deluge, delugevpn, and transmission-openvpn.

        Conflict: Yes. You’ll need to resolve this by remapping one or more services.

    Port 8080:

        Used by gluetun, sabnzbdvpn, and transmission-openvpn.

        Conflict: Yes. Remap one or more services.

    Port 9091:

        Used by gluetun, sabnzbdvpn, and transmission.

        Conflict: Yes. Remap one or more services.

    Port 6789:

        Used by nzbget, nzbgetvpn, and transmission-openvpn.

        Conflict: Yes. Remap one or more services.

    Port 51413:

        Used by gluetun, sabnzbdvpn, and transmission.

        Conflict: Yes. Remap one or more services.

    Port 8090:

        Used by mylar3 and sabnzbdvpn.

        Conflict: Yes. Remap one or both services.

    Port 5055:

        Used by overseerr and jellyseerr (5056).

        Conflict: No, but close. Ensure these ports are not remapped to the same port.

Recommendations

To resolve conflicts:

    Remap conflicting ports:

        For example, change 8112 to 8113 for one of the services.

        Change 8080 to 8081 for one of the services.

        Change 9091 to 9092 for one of the services.

    Use unique ports:

        Ensure each service has a unique port mapping to avoid conflicts.

    Test configurations:

        After remapping, test the services to ensure they work as expected.

