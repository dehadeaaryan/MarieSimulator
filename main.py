from Marie import Marie
from MarieReader import MarieReader as mr

def main():
    marie = Marie(mr('trial'))
    marie.show()
    marie.run()
    marie.show()

main()