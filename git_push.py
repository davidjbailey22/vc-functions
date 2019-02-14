'''
add, commit and push a file to master repo using Python (if using command line)
need to install GitPython first
by D. Bailey
'''

from git import Repo
import os.path

def git_push():

    # Change to your local cloned repo
    local_repo = r''

    # add file you wish to add to staging, commit, and push to master
    print "What file do you want to add/commit/push?"
    f = raw_input()

    # find file name in repo
    def find(fname, path):
        for root, dirs, files in os.walk(path):
            # exclude .git
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']
            if fname in files:

                # gets path for the input file
                input_file = os.path.join(root, fname)
                print input_file

                # add commit comment
                print "Add a comment message for " + fname
                comment = raw_input()

                # add, commit and push commands to master Git repo
                repo = Repo(local_repo)
                repo.git.add(input_file)
                repo.index.commit(comment)
                repo.git.push("origin")
                print "Code successfully pushed!"

            else:
                print "No file exists in Repo"

    find(f, local_repo)

git_push()
