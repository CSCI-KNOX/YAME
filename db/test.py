import retrieve_from_db
import sys

def main():

    retrieve_from_db.getOne('channels')
    print (retrieve_from_db.howManyAreSame('channels'))
if __name__ == "__main__":
    main()
