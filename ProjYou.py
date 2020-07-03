import sqlite3 as lite

# functionality goes here
class DatabaseManage(object):
    
    def __init__(self):
        global con
        try:
            con = lite.connect('videos.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS video(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT,tags TEXT)")
        except Exception:
            print("Unable to create a DB !")
            
    # TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO video(name, description, tags) VALUES (?,?,?)", data
                    )
                return True
        except Exception:
            return False

    # TODO: read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM video")
                return cur.fetchall()
        except Exception:
            return False

    # TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM video WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False


# TODO: provide interface to user

def main():
    print("*"*40)
    print("\n:: YOUTUBE VIDEO IDEAS :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('\nPress 1. Insert a new Youtube video idea\n')
    print('Press 2. Show all video ideas\n')
    print('Press 3. Delete a video idea (NEED ID OF VIDEO)\n')
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice: ")

    if choice == "1":
        name = input("\n Enter video name: ")
        description = input("\n Enter video description: ")
        tags = input("\n Enter tags for video: ")
        
        if db.insert_data([name, description, tags]):
            print("Video Idea was inserted successfully")
        else:
            print("OOPS SOMETHING WENT WRONG")


    elif choice == "2":
        print("\n:: Youtube Video Ideas List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("Video ID : " + str(item[0]))
            print("Video Name : " + str(item[1]))
            print("Video Description : " + str(item[2]))
            print("Tags for video : " + str(item[3].split(',')))
            print("\n")

    elif choice == "3":
        record_id = input("Enter the video ID: ")

        if db.delete_data(record_id):
            print("Course was deleted with a success")
        else:
            print("OOPS SOMETHING WENT WRONG")

    else:
        print("\n BAD CHOICE")      

if __name__ == '__main__':
    main()