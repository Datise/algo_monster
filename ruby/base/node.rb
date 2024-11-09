class Node
  attr_accessor :val, :left, :right
  def initialize(val, left, right)
    self.val = val 
    self.left = left
    self.right = right
  end
end


class NonBNode
  attr_accessor :val, :children
  def initialize(val, children=[])
    self.val = val 
    self.children = children 
  end
end