# (Prometheus) Pushgateway

This is a hack to get `pushgateway` into a container using `pack` so it can be deployed on Toolforge.

It is slightly less terrible than the previous solution of dumping the pre-compiled binary onto NFS then executing it in a container.

Once T401075 / T363027 is resolved, this can be replaced.

## Logic
* `setup.py` handles setting up the container image (downloading the binary)
* `entrypoint.py` handles setting up the runtime (config)

## Testing locally
```
$ pack build --builder heroku/builder:24 external-pushgateway
```
