# Club Checker
from pyscript import display, document

def view_club(e):
    document.getElementById('result').innerHTML = ' '
    verifclubmember = ['Dwayne Chua', 'Marcus Viray', 'Jesse Villante', 'Kaizer Chua', '6 7']
    firstname = document.getElementById('fname').value
    lastname = document.getElementById('lname').value
    unverifclubmember = str(firstname) + " " + str(lastname)
    club_member_checker = unverifclubmember in verifclubmember

display_message = (f'Sorry {unverifclubmember}, your name is not on the list.', f'Congratulations {unverifclubmember}! You are now part of the Unknown Club.')
display(display_message[club_member_checker], target='result')