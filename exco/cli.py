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
            print("Enter a command:")
            print("1. List all resources")
            print("2. Delete a resource")
            print("3. Exit")
            command = input()
            if command == '1':
                resources = Resource.query.all()
                for resource in resources:
                    print(resource)
            elif command == '2':
                print("Enter the ID of the resource you want to delete:")
                resource_id = input()
                resource = session.get(Resource, resource_id)
                if resource:
                    session.delete(resource)
                    session.commit()
                    print(f"Resource with ID {resource_id} deleted.")
                else:
                    print(f"Resource with ID {resource_id} not found.")
            elif command == '3':
                break
            else:
                print("Invalid command. Please try again.")