# Punto de partida para el TP 1 de Arquitectura de Software (75.73) del 1er cuatrimestre de 2019

> **La fecha de entrega para el informe y el código es el jueves 25/04** :bangbang:

La forma de entrega será crear un canal **privado** en Slack (llamado como el grupo) con todos los miembros del grupo y todos los docentes, y poner ahí un link al repositorio con el código (en caso de ser privado, invitar también a todos los docentes) y el informe (o avisar si está en el repositorio).

El informe puede ser un PDF, Google Doc o Markdown/Wiki en el mismo repositorio del código. **Debe** incluir screenshots del dashboard de métricas para cada caso analizado que permitan observar los resultados obtenidos.

## Objetivos

El objetivo principal es comparar algunas tecnologías, ver cómo diversos aspectos impactan en los atributos de calidad y probar, o al menos sugerir, qué cambios se podrían hacer para mejorarlos.
El objetivo menor es que aprendan a usar una variedad de tecnologías útiles y muy usadas hoy en día, incluyendo:

- Node.js (+ Express)
- Python (+ Flask y Gunicorn)
- Docker
- Docker-compose
- Nginx
- Algún generador de carga (la propuesta es usar Artillery, pero pueden cambiarlo)
- Alguna forma de tomar mediciones varias y visualizarlas, preferentemente en tiempo real, con persistencia, y en un dashboard unificado (la propuesta es usar el plugin de Artillery + cAdvisor + StatsD + Graphite + Grafana, pero pueden cambiarlo).

## Consigna

Implementar un servicio HTTP en dos tecnologías diferentes (Node.js-Express y Python-Gunicorn). Someter distintos tipos de endpoints a diversas intensidades/escenarios de carga en algunas configuraciones de deployment, tomar mediciones y analizar resultados.

A partir de este repositorio como punto inicial, van a tener que implementar cada webserver y dockerizarlo (completar las carpetas `js/` y `py/` de este repositorio), agregar los servicios con esos webservers al `docker-compose.yml`, y configurar las locations y upstreams de nginx en `nginx_reverse_proxy.conf`.

Para generar carga y ver las mediciones obtenidas, en la carpeta `perf/` tienen un dashboard de Grafana ya armado (`dashboard.json`) y un ejemplo de un escenario básico de artillery. También hay un script y una configuración en el `package.json` para que puedan ejecutar los escenarios que hagan corriendo:

```sh npm run scenario <filename> <server>```

donde `<filename>` es el nombre del archivo con el escenario (sin la extensión `.yaml`) y `<server>` es el server contra el que quieren ejecutarlo (vean la sección `environments` dentro del yaml del escenario).

> Queda a cargo de cada grupo elegir qué endpoints y configuraciones de deployment prueba bajo qué escenarios de carga.
> **Es preferible armar pocos casos y analizarlos lo más posible que juntar muchísima información y estudiar poco los
> resultados.** :warning:

### Tipos de endpoints para comparar los servidores

#### Obligatorios

| Caso | Implementado como | Representa |
| ---- | ----------------- | ---------- |
| Ping | Respuesta de un valor constante (rápido y de procesamiento mínimo) | Healthcheck básico |
| Proxy/timeout | Duerme cierto tiempo y responde (lento y de procesamiento mínimo) | Llamada a otro servicio (request HTTP, llamada a DB, etc.) casi sin procesamiento de datos. |
| Intensivo | Loop de cierto tiempo (lento y de alto procesamiento) | Cálculos pesados sobre los datos (ej: algoritmos pesados, o simplemente muchos cálculos) |

#### Opcionales

| Caso | Implementación |
| ---- | -------------- |
| Contenido estático | El endpoint responde con un archivo estático fijo. Pueden probarlo con archivos chicos y con archivos grandes |
| Proxy (verdadero) | Pueden hacer que el server llame a otro servicio suyo, que demore lo mismo que demoraba el caso proxy/timeout anterior, y comparar |
| ... | ... pueden agregar otros casos que se les ocurran |

### Configuraciones de deployment

> **Todo el tráfico debe pasar por el nginx en todos los casos, para que todos tengan la latencia del salto "extra"**

#### Obligatorias

| Caso | Explicación |
| ---- | ----------- |
| Node | Servidor en node, con un solo proceso. Un solo container. |
| Gunicorn | Servidor en python con gunicorn, usando un solo worker sincrónico (el del tipo default). Un solo container. |
| Replicado | Alguno de los casos anteriores (node o python) replicado en múltiples containers, con load balancing a nivel de nginx |

#### Opcionales

| Caso | Explicación |
| ---- | ----------- |
| Multi-worker | Para una o varias de las configuraciones obligatorias, pueden probar manejar más de un worker en cada container (usar siempre la misma cantidad). Vean el flag `-w` de Gunicorn y el módulo `cluster` ([v8.x](https://nodejs.org/docs/latest-v8.x/api/cluster.html) o [v10.x](https://nodejs.org/docs/latest-v10.x/api/cluster.html)) de Node.js |
| Servidor remoto | Todos los casos anteriores suponen que el servidor corre en la misma computadora física que el cliente (generador de carga). Pueden probar montar uno o varios de ellos en otra computadora (otra en la misma casa, o un servidor en algún proveedor cloud) y comparar las métricas al "alejar" cliente de servidor. Consideren en el análisis también que las características de la computadora corriendo el servidor o el cliente pueden cambiar en esos casos. |
| ... | ... pueden agregar otros casos que se les ocurran |

Para aquellos que prueben endpoints de contenido estático, también pueden probar que el nginx sirva el contenido estático directamente. En casos en que vayan a tomar medidas del nginx, consideren que también se puede configurar la cantidad de workers de nginx, y deberían usar la misma cantidad que usen en los otros servidores (cuando es nginx el que sirve el contenido)
para poder comparar de manera más justa.

### Generación de carga para las pruebas

Hay muchos tipos de escenarios de carga y pruebas de performance en general. Pueden leer por ejemplo [acá](https://www.softwaretestingclass.com/what-is-performance-testing/) (o en cualquiera de los miles de links al googlear sobre el tema) sobre algunos tipos de escenarios que pueden implementar. Queda a decisión de cada grupo elegir cuáles implementar, considerando siempre cuál es el que más útil les resulta para analizar lo que quieran estudiar.

-----------

## Links útiles

- Nodejs:
  - https://nodejs.org/
  - https://github.com/creationix/nvm
  - https://nodejs.org/dist/latest-v8.x/docs/api/ o https://nodejs.org/dist/latest-v10.x/docs/api/
- Express:
  - http://expressjs.com/en/starter/hello-world.html
- Python:
  - https://www.python.org/
  - https://docs.python.org/2/ o https://docs.python.org/3/
- Flask:
  - http://flask.pocoo.org/
  - http://flask.pocoo.org/docs/1.0/
- Gunicorn:
  - https://gunicorn.org/
  - http://docs.gunicorn.org/en/latest/index.html
- Nginx:
  - https://nginx.org/
- Docker:
  - http://docker-k8s-lab.readthedocs.io/en/latest/docker/docker-engine.html
  - https://www.docker.com/
- Docker-compose:
  - https://docs.docker.com/compose/
- StatsD:
  - https://github.com/etsy/statsd
  - https://github.com/etsy/statsd/blob/master/docs/graphite.md
- Graphite:
  - https://graphiteapp.org/
  - https://graphite.readthedocs.io/en/latest/
- Grafana:
  - https://grafana.com/
  - http://docs.grafana.org/guides/getting_started/
- imagen usada (statsd + graphite):
  - https://hub.docker.com/r/graphiteapp/graphite-statsd/
  - https://github.com/graphite-project/docker-graphite-statsd
- Gotchas:
  - http://dieter.plaetinck.be/post/25-graphite-grafana-statsd-gotchas/
- Artillery:
  - https://artillery.io/docs/
  - https://www.npmjs.com/package/artillery
  - https://www.npmjs.com/package/artillery-plugin-statsd

## Pequeño cheatsheet de docker

Es posible que necesiten ejecutar los comandos con `sudo`, según el sistema que usen y cómo lo hayan instalado.

```sh
# Ver qué containers existen
docker ps [-a]

# Ver qué imagenes hay en mi máquina
docker images

# Ver uso de recursos de containers (como "top" en linux)
# Ejemplo con formato específico: docker stats --format '{{.Name}}\t{{.ID}}\t{{.CPUPerc}}\t{{.MemUsage}}'
docker stats [--format <format_string>]

# Descargar una imagen
docker pull <image>[:<tag>]

# Eliminar un container
docker rm <container_id> [-f]

# Eliminar una imagen
docker rmi <image_id> [-f]

# Eliminar imágenes "colgadas" (dangling)
docker rmi $(docker images -q -f dangling=true)

# Versión instalada
docker version
```

## Pequeño cheatsheet de docker-compose

Todos los siguientes comandos deben ejecutarse desde la carpeta en donde está el archivo `docker-compose.yml` del proyecto.

Es posible que necesiten ejecutar los comandos con `sudo`, según el sistema que usen y cómo lo hayan instalado.

```sh
# ALIAS para escribir menos nomás
alias docc='docker-compose'

# Ayuda general
docc --help

# Ayuda genral para cualquier comando
docc [COMMAND] --help

# Levantar servicios.
# Sugerencia: Usar la opción -d para levantar en background, y poder seguir usando la terminal
# También sirve para escalar horizontalmente un servicio que ya se esté ejecutando [buscar opción --scale].
# Si no se especifica al menos un servicio, se levantan todos
docc up [options] [SERVICE...]

# Ver logs de un servicio ejecutándose en background
docc logs [options] [SERVICE]

# Listar containers y sus estados
docc ps

# Restartear servicios
# Si no se indica al menos un servicio, se restartean todos
docc restart [SERVICE...]

# Frenar servicios corriendo en background (con la opción --detach del `up`)
# Si no se lista ningún servicio, se frenan todos.
# Esto solo frena servicio, no borra el container ni los datos que hayan en el mismo
docc stop [SERVICE...]

# Frenar containers y borrar tanto los containers como las imágenes y los volúmenes de almacenamiento
# (se pierden todos los datos que hubiera en el container).
# Esto aplica a TODOS los levantados con `up`, no filtra por servicio
docc down

# Levantar un nuevo container de un servicio y ejecutar un comando adentro
# (util para tener por ejemplo una terminal dentro de un container e inspeccionarlo o hacer pruebas manuales).
# Como es siempre sobre un container nuevo, lo que ven es el resultado de su docker-compose.yml y sus dockerfiles
# Ejemplo: docc run graphite bash
docc run SERVICE COMMAND

# Correr un comando en un container que ya existe y ya está corriendo.
# Parecido a `run` pero sobre un container en ejecución.
# Útil para alterar o inspeccionar algo que se está ejecutando.
#Lo que ven adentro puede no ser el resultado directo del docker-compose.yml + dockerfiles, así que mucho cuidado
# si van a modificar sus containers así, porque puede ser difícil de reproducir luego.
# Ejemplo: docc exec graphite bash
docc exec SERVICE COMMAND

# Versión instalada
docc version
```