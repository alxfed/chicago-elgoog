from google.cloud import bigtable

client = bigtable.Client(project='chicago-elgoog', admin=True)

# instances = client.list_instances()

location_id = 'us-central1-c'
display_name = 'first-instance'
instance_id = 'instance-1'
instance = client.instance(instance_id, location_id,
                           display_name=display_name)

operation = instance.create()

print(operation.finished())

instance.reload()

client.display_name = 'not-first-instance'
instance.update()

tables = instance.list_tables()

table_id = 'first-table'

table = instance.table(table_id)
table.create()

table.delete()

instance.delete()

print('ok')
