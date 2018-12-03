from keystoneauth1 import loading, session, adapter
from heatclient import client
from os import environ


def get_heat_client():
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(
        auth_url=environ['OS_AUTH_URL'],
        username=environ['OS_USERNAME'],
        password=environ['OS_PASSWORD'],
        project_id=environ['OS_PROJECT_ID'],
        OS_USER_DOMAIN_NAME=environ['OS_USER_DOMAIN_NAME'])
    sess = session.Session(auth=auth)
    adp = adapter.Adapter(
        session=sess, region_name=environ['OS_REGION_NAME'])

    return client.Client('1', session=adp)


def get_stack_output(key):
    heat = get_heat_client()
    output = heat.stacks.output_show(environ['STACK_ID'], key)
    return output['output']['output_value']
