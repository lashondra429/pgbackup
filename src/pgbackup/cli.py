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

def main():

    import boto3, time
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()

    dump = pgdump.dump(args.url)
    timestamp = time.strftime("%Y-%m-%dT%H:%M",time.localtime())
    file_name=pgdump.dump_file_name(args.url, timestamp)
    
    if args.driver == 's3':
        client = boto3.client('s3')
        print(f"Backing database up to {args.destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile=open(file_name,'wb')
        print(f"Backing datatbase up to locally to {outfile.name}")
        storage.local(dump.stdout, outfile)
