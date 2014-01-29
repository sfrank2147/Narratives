import re 

def yes_value(response):
    '''Returns True if a response is intended to be a Yes
       Returns False if a response is intended to be a No
       Returns None if response is blank or irrelevant'''
    if response.lower() in ['yes','y']:
        return True
    elif response.lower() in ['no','n']:
        return False
    else:
        return None

def gender(response):
    '''Returns dictionary of gender pronouns for student'''
    if response.lower() in ['male','m','boy','b']:
        return {'subject':'he','object':'him', 'possessive':'his'}
    
    #guarantees a response
    else:
        return {'subject':'she','object':'her','possessive':'her'}

def grades(student):
    response = "{0}'s semester grade in Geometry is {1:.0f}%.  The breakdown of "\
               "this is {2:.0f}% exams/quizzes, {3:.0f}% homework, {4:.0f}% participation"\
               ", and {5:.0f}% binder.".format(student['name'],student['average'],
                                           student['exams/quizzes'],student['homework'],
                                           student['participation'],student['binder'])
    return response

def participation(student):
    gender_nouns = gender(student['gender'])
    part_level = student['level of participation']
    if(part_level in ['H','h']):
        response = 'In class, {0} is respectful, engaged, and a strong participant.'\
                    ' {1} always manages to push the class forward in discussion by'\
                    ' commenting on what other students have to say or offering new'\
                    ' questions to consider. {0} also works well with {3} peers.'\
                    .format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    elif(part_level.lower() == 'm'):
        response = 'In class, {0} is respectful, engaged, and a strong participant.'\
                    ' {1} works well with {3} peers.  I would like to see {0} participate'\
                    ' even more next semester by partaking in "Be the Teacher" presentations.'\
                    ' This would be a good opportunity for {0} to engage in discussion since'\
                    ' {1} has many insightful points that the class would benefit from hearing and'\
                    ' seeing demonstrated.'\
                    .format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    elif(part_level.lower() == 'lgn'):
        response = 'In class, {0} is hardworking and engaged.  However, {1} does not participate'\
                   ' enough.  Active participation is essential for full credit every day.  It is also an important'\
                   ' part of being a member of a community of learners.  I encourage {2} to raise {3} hand'\
                   ' and answer questions at least 2 times every class.'\
                    .format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    elif(part_level.lower() == 'lbn'):
        response = 'In class, {0} is often disengaged and fails to keep up with notes.  {1} is therefore'\
                   ' missing a crucial study tool.  When it is time to do practice problems, {1} quickly falls behind.  This may'\
                   ' be because {1} has no examples to refer to.  This lost practice has been carrying over to {0}\'s exam grades as well.'\
                    .format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    #silently return none if user screws up
    return response

def on_time(student):
    gender_nouns = gender(student['gender'])
    if yes_value(student['on time?']):
        return ''
    else:
        response = '{0}\'s consistent latenesses have limited {3}\'s performance in this course.'\
                    ' I encourage {0} to be proactive about learning missed material in a timely manner in order to get back on track'\
                    .format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
        return response

def avg_with_hw(student):
    gender_nouns = gender(student['gender'])
    if not yes_value(student['include possible average with all homework?']):
        return ''
    else:
        response = '{0} should work on improving in the homework component of this class for next semester.'\
                   ' If {1} had submitted all homework assignments complete and on time, {3} class average'\
                   ' would have been {4:.0f}%.  This is a significant difference.'\
                    .format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'],student['20-(e/100)(20)+c'])
        return response

def improve_exams(student):
    gender_nouns = gender(student['gender'])
    if yes_value(student['improve on exams?']):
        response = 'Next semester, {0} should focus on improving {3} exam scores. To better prepare for exams, {0} should cover up completed classwork and redo the same problems. {4} can then check {3} new answers with {3} old answers.'\
                   .format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'], gender_nouns['subject'].upper())
    else:
        response = 'I commend {0} for {3} strong performance on exams and hope to see this consistent performance next semester as well! '.format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    return response

def attend_tutoring(student):
    gender_nouns = gender(student['gender'])
    if yes_value(student['should attend tutoring?']):
        return 'I recommend that {0} attend tutoring on Thursdays before exams or whenever {1} struggles to complete homework assignments.'.format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    else:
        return ''

def mastery(student):
    gender_nouns = gender(student['gender'])
    if (student['mastery/final sentence'].lower() == 'good'):
        response = '{0} has mastery in all major topics covered this semester and therefore does not have an MBA.  If {0} takes the next steps above, I am confident that {1} will be successful next semester.'.format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    else:
        response = '{0} is missing mastery in every topic covered this semester and will therefore have an MBA.  {0} must work on improving in all the areas mentioned above in order to be successful next semester.'.format(student['name'],gender_nouns['subject'],gender_nouns['object'], gender_nouns['possessive'])
    return response

    

# #functions for generating strings based on response of user
# def average(student):
#     response = ''
#     try:
#         response = "{0} currently has an average of {1:.0f}. ".format\
#                             (student['name'],student['current average'])
#     except KeyError:
#         pass
#     return response
# 
# def participates(student):
#     gender_nouns = gender(student['gender'])
#     if yes_value(student['participates?']):
#         return ('{0} always manages to push the class forward in mathematical'
#                 ' discussion by commenting on what other students have to say'
#                 ' or offering new questions to consider. '
#                 ).format(gender_nouns['subject'].capitalize())
#     else:
#         return ('{0} could get more out of this class if {1} participated '
#                 'more actively. ').format(gender_nouns['subject'].capitalize(),
#                                           gender_nouns['subject'])
# 
# def strong_ability(student):
#     gender_nouns = gender(student['gender'])
#     if yes_value(student['strong math ability?']):
#         return ('{0} is a student with strong mathematical ability. '
#                 ).format(student['name'].capitalize())
#     else:
#         return ''
# 
# def does_homework(student):
#     gender_nouns = gender(student['gender'])
#     if not yes_value(student['does homework?']):
#         return('{0} does not finish {2} homework regularly and on time. '
#                'If {1} did, it would help {2} grade significantly. '
#                ).format(student['name'].capitalize(),gender_nouns['subject'],
#                         gender_nouns['possessive'])
#     else:
#         return ''
# 
# def on_time(student):
#     gender_nouns = gender(student['gender'])
#     if not yes_value(student['on time?']):
#         return ('{0} is frequently late to class, which is significantly '
#                 'impacting {1} performance. '
#                 ).format(student['name'].capitalize(),gender_nouns['possessive'])
#     else:
#         return ''
# 
# def tutoring(student):
#     gender_nouns = gender(student['gender'])
#     if yes_value(student['should attend tutoring?']):
#         return ('{0} should attend tutoring regularly in order to make sure '
#             'that {1} succeeds in my class. '
#              ).format(student['name'].capitalize(), gender_nouns['subject'])
#     else:
#         return ''
# 
# def additional_comments(student):
#     try:
#         return student['additional comments?']
#     except KeyError:
#         return ''

def first_name(student):
    full_name = student['name']
    names = full_name.split()
    if len(names) > 1:
        return names[1]
    else:
        return full_name
    

def narrative(student):
    #make sure only use first name in narrative
    student['name'] = first_name(student)
    
    #generate narrative
    narrative = ''
#     narrative += average(student)
#     narrative += strong_ability(student)
#     narrative += participates(student)
#     narrative += does_homework(student)
#     narrative += on_time(student)
#     narrative += tutoring(student)
#     narrative += additional_comments(student)
    narrative += grades(student) + ' '
    narrative += participation(student) + ' '
    narrative += on_time(student) + ' '
    narrative += avg_with_hw(student) + ' '
    narrative += improve_exams(student) + ' '
    narrative += attend_tutoring(student) + ' '
    narrative += mastery(student) + ' '
    narrative += student['additional comments?']
    
    narrative = re.sub(r'( )+',r' ',narrative)
    
    return narrative
