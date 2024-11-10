class Node
  attr_accessor :val, :left, :right, :children
  def initialize(val, left, right)
    self.val = val 
    self.left = left
    self.right = right
    self.children = [self.left, self.right]
  end

  def print 
    base = "#{self.val}"
    base += self.left ? base + " left: #{self.left.val}" : base
    base += self.right ? base + " right: #{self.right.val}" : base
    puts base
  end
end


class NonBNode
  attr_accessor :val, :children
  def initialize(val, children=[])
    self.val = val 
    self.children = children 
  end
end