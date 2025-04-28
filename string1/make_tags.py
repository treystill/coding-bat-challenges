def make_tags(tag, word):
  tag1 = '<' + tag + '>'
  tag2 = '<' + '/' + tag + '>'
  return tag1 + word + tag2
