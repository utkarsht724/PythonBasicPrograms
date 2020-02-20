#Python program to count the values associated with key in a dictionary
Sample_data= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
                {'id': 3, 'success': True, 'name': 'Alex'}]
print(Sample_data)
print(sum(d['success'] for d in Sample_data))
