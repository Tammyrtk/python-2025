criteria = ['economical', 'durable', 'fast']

candidates = {
    'accord': {'shaft issue', 'fast', 'good design', 'electrical'},
    'corolla': {'fast', 'economical', 'durable', 'oversaturated'},
    'model x': {'fast', 'electric', 'y-wheel', 'economical', 'durable'},
    'civic': {'ayooo', 'hybrid', 'durable'},
    'sonata': {'eco friendly', 'stylish', 'durable', 'economical', 'fast'},
}

interviewees = set()
for candidate, skills in candidates.items():
    #if skills.issuperset(criteria):
    if skills > set(criteria):
        interviewees.add(candidate)

print(interviewees)
