
explanation = """
This is a CLI for interacting with the Exco database, mostly for managing and deleting resources.

Current commands:
- 'help': Print this explanation
- 'list': List all resources in the database
- 'delete [ID1, ID2, ...]': Delete resources with the given IDs
- 'insert [count]': Insert mock resources into the database
- 'recreate': Recreate the database tables
- 'exit': Exit the CLI
"""

print(explanation)

try:
    from exco.extensions import db
    from exco.app import app
    from exco.models import Resource
except ImportError:
    from extensions import db
    from app import app
    from models import Resource


if __name__ == '__main__':
    with app.app_context():
        session = db.session
        while True:
            # Match statement for different commands\
            print("Enter command ('help' for help): ", end='')
            command = input()
            match command.split():
                case ['help']:
                    print(explanation)
                case ['list']:
                    resources = session.query(Resource).all()
                    for resource in resources:
                        print(resource)
                case ['delete']:
                    print("Enter the IDs of the resources you want to delete, separated by spaces")
                    continue
                case ['delete', *file_ids]:
                    for file_id in file_ids:
                        resource = session.get(Resource, file_id)
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
                case ['recreate']:
                    if input("Are you sure you want to recreate the database tables? This will destroy all data. (y/N) ") == 'y':
                        session.drop_all()
                        session.create_all()
                        print("Recreated database tables.")
                case ['exit']:
                    break
                case _:
                    print("Invalid command. Type 'help' for help.")
        session.commit()
        session.close()
