
prompt = input('Enter score between 0.0 - 1.0')
try:
    score = float(prompt)
except:
    print('Please Enter A Number!')

if score > 1:
    print('Bad Score!')
elif score >= 0.9:
    print('Grade: A')
elif score >= 0.8:
    print('Grade: B')
elif score >= 0.7:
    print('Grade C')
elif score >= 0.6:
    print('Grade: D')
elif score < 0.6:
    print('Grade: F')
