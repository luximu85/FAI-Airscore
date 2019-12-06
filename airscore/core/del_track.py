"""
Delete track and all references in other tables
Use: python3 del_track.py [traPk]

Antonio Golfari - 2019
"""
# Use your utility module.
from myconn import Database
from db_tables import tblTaskResult as R

def delete_track(result_id):

    with Database() as db:
        q       = db.session.query(R)
        result  = q.get(result_id)
        file    = result.traFile
        db.session.delete(result)
        db.session.commit()

    if p.isfile(file):
        os.remove(file)
        print(f'Track file has been deleted \n')
    else:
        print("Couldn't find a Track file for this result \n")

    if result:
        print(f"Result with ID: {result_id} succesfully deleted \n")
        return 1
    return 0

def main(args):
    from logger import Logger
    '''create logging and disable output'''
    Logger('ON', 'task_full_rescore.txt')

    print("starting..")
    '''Main module. Takes traPk as parameter'''
    track_id = 0 + int(args[0])

    """Delete track"""
    out = delete_track(track_id)

    ''' now restore stdout function '''
    Logger('OFF')

    ''' output ref_id to use in frontend:
        task_result.php?refPk=ref_id&tasPk=task_id&comPk=comp_id'''
    print(f'{out}')

if __name__ == "__main__":
    import sys
    '''check parameter is good'''
    if not (sys.argv[1] and sys.argv[1].isdigit() and int(sys.argv[1]) > 0):
        print("number of arguments != 1 and/or track_id not a number")
        print("usage: python3 del_track.py <traPk>")
        exit()

    main(sys.argv[1:])