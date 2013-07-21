message_data = {
  'q-health-insurance' : 
    {
      'kind': 'question',
      'answer_options': [1, -1],
      'next_message':{1:'q-coverage-type', 
                      -1:'reasons-to-enroll'}
    },
  'q-coverage-type' :
    {
      'kind': 'question',
      'answer_options': [1, 2, 3, 4],
      'next_message':{1:'private',
                      2:'medi-cal',
                      3:'sf-path',
                      4:'healthy-sf'
                      }
    },
  'private' : 
    {
      'kind': 'statement',
      'answer_options': None,
      'next_message':None
    },
  'medi-cal' : 
    {
      'kind': 'statement',
      'answer_options': None,
      'next_message':None
    },
  'sf-path' : 
    {
      'kind': 'statement',
      'answer_options': None,
      'next_message':None
    },
  'healthy-sf' : 
    {
      'kind': 'statement',
      'answer_options': None,
      'next_message':None
    }
}