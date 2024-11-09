class Node
  attr_accessor :val, :left, :right, :children
  def initialize(val, left, right)
    self.val = val 
    self.left = left
    self.right = right
  end

  def children
    [self.left, self.right]
  end
end


class NonBNode
  attr_accessor :val, :children
  def initialize(val, children=[])
    self.val = val 
    self.children = children 
  end
end