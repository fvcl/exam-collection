# This file is a CLI for interacting with the Exco database, mostly for managing and deleting resources.

# Path: exco/cli.py
try:
    from exco.exco import Resource, app, db
except ImportError:
    from exco import Resource, app, db
if __name__ == '__main__':
    with app.app_context():
        session = db.session
        while True:
            # Match statement for different commands\
            print("Enter command ('help' for help): ", end='')
            command = input()
            match command.split():
                case ['help']:
                    print("Commands: 'insert', 'list', 'delete ID1 ID2 [...]', 'exit'")
                case ['list']:
                    resources = session.query(Resource).all()
                    for resource in resources:
                        print(resource)
                case ['delete']:
                    print("Enter the IDs of the resources you want to delete, separated by spaces")
                    continue
                case ['delete', *file_ids]:
                    for file_id in file_ids:
                        resource = session.query(Resource).get(file_id)
                        if resource:
                            session.delete(resource)
                            print(f"Deleted {resource}")
                        else:
                            print(f"Resource with id {file_id} not found.")
                case ['insert']:
                    print("Enter the number of mock resources to insert")
                    continue
                case ['insert', count]:
                    for _ in range(int(count)):
                        resource = Resource.generate_dummy_resource()
                        session.add(resource)
                    print(f"Added {count} mock resources.")
                case ['exit']:
                    break
                case _:
                    print("Invalid command. Type 'help' for help.")
        session.commit()
        session.close()
