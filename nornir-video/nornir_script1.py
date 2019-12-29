from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get

nr = InitNornir(
        config_file="config.yaml", dry_run=True
)

results = nr.run(
        task=napalm_get, getters=["facts", "interfaces", "arp_table"]

)

print_result(results)
