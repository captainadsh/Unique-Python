import os

def create_on_desktop():
    file_name = input("Enter filename with extension: ")
    dir = os.path.join('C:\\Users\\%s\\Desktop\\%s' %(os.getlogin(), file_name))
    fhand = open(dir, 'w')
    fhand.close()

def main():
    create_on_desktop()

if __name__ == '__main__':
    main()
