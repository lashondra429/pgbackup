from argparse import ArgumentParser, Action

known_drivers = ["local", "s3"]

class DriverAction(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values

        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local' &'s3")
        namespace.driver = driver.lower()
        namespace.destination = destination
        

def create_parser():
    parser=ArgumentParser(description = "Back up PostgreSQL databases locally or to AWS S3")
    parser.add_argument("url", help = "URL of the DB to backup")
    parser.add_argument("--driver", help="how & where to store the backup", nargs=2, required=True, action=DriverAction)

    return parser