make dockdown-cent
make dockdown-clust
make dockdown-dist

export APP=auction1
export GRANULARITY=1
export LOCKTYPE=1

make dockrun-cent
# make dockrun-clust
# make dockrun-dist