from dbModels.models import Agent,Party, State

# users value
users = [(1, 'Christian', 'Emenike', 'christian@bincom.net', '08034699500', 1),
(2, 'Ngozi', 'Emenike', 'biggysmalls@home.net', '08089003444', 2),
(3, 'Chinyere', 'Emenike', 'chinyere@emenike.net', '07034532310', 1),
(4, 'Chimezie', 'Emenike', 'chimezie@emenike.net', '07034532322', 2)]

# for u in users:
#     print(f'username={u[1]}, phone={u[4]}')

# required field agent
"""
Email: clemcy9@gmail.com
Username: clement
Phone: 08020366909
Pollingunit uniqueid: 1
Password:
Password (again):
"""

# script
for user in users:
    a = Agent(first_name=user[1],last_name=user[2],email=user[3],phone=user[4],pollingunit_uniqueid=user[5])
    a.save()



# party values
parties =[(1, 'PDP', 'PDP'),
(2, 'DPP', 'DPP'),
(3, 'ACN', 'ACN'),
(4, 'PPA', 'PPA'),
(5, 'CDC', 'CDC'),
(6, 'JP', 'JP'),
(7, 'ANPP', 'ANPP'),
(8, 'LABOUR', 'LABOUR'),
(9, 'CPP', 'CPP')
]

# script

for p in parties:
    party = Party(party_id = p[1],party_name = p[2])
    party.save()

# states values
states = [
    (1, 'Abuja'),
(2, 'Abia'),
(3, 'Anambra'),
(4, 'Akwa Ibom'),
(5, 'Adamawa'),
(6, 'Bauchi'),
(7, 'Bayelsa'),
(8, 'Benue'),
(9, 'Borno'),
(10, 'Cross River'),
(12, 'Ebonyi'),
(13, 'Edo'),
(14, 'Ekiti'),
(15, 'Enugu'),
(16, 'Gombe'),
(17, 'Imo'),
(18, 'Jigawa'),
(19, 'Kaduna'),
(20, 'Kano'),
(21, 'Katsina'),
(22, 'Kebbi'),
(23, 'Kogi'),
(24, 'Kwara'),
(25, 'Delta'),
(26, 'Nasarawa'),
(27, 'Niger'),
(28, 'Ogun'),
(29, 'Ondo'),
(30, 'Osun'),
(31, 'Oyo'),
(32, 'Plateau'),
(33, 'Rivers'),
(34, 'Sokoto'),
(35, 'Taraba'),
(36, 'Yobe'),
(37, 'Zamfara'),
(251, 'Lagos')
]

# script
for s in states:
    state = State(state_id =s[0], state_name =s[1])
    state.save()