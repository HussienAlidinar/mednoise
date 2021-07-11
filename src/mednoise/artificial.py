def artificial_complete():
  """
  Processes inputted images using a jaccard-similarity algorithm, similar to the ones used in machine learning and deep learning. Allows a user to selectively filter instances of noise that may be slightly different with each image.
  
  Parameters
  ----------
  filepath: string
    A filepath for images to be selected from. Since **mednoise** uses ``glob``, it can take any argument that ``glob`` can parse through.
  find: RGB tuple
    A value that indicates silenced noise. Usually is considered the background color of the input image, often ``(0,0,0)``.
  matrix: tuple
    A series of ``x, y`` coordinates that defines opposite coordinates of a rectangular selection of a picture. This is passed as a number-tuple, in the format ``(x1, y1, x2, y2)``. Used to compare similarity and forms the basis of this algorithm.
  
  Notes
  -----
  This algorithm is objectively contains the most complex and computing-intensive calculations. It should only be used as a last resort after trying other algorithms unsuccessfully, or in the case of high-performance computing.

  Examples
  --------
  >>> md.artificial_complete()
  This feature is still being worked on.
  """
  print("This feature is still being worked on.")
  
def artificial_calculator():
  print("This feature is still being worked on.")
  
def artificial_analyzer():
  print("This feature is still being worked on.")
  
def artificial_isolator():
  print("This feature is still being worked on.")
