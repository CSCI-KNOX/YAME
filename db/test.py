import retrieve_from_db
import sys

def main():
    name = sys.argv[1].replace(' ', '+')+' '

    retrieve_from_db.getOne(name)
if __name__ == "__main__":
    main()
