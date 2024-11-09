require 'pry'
require_relative '../base/node'

class BTree
  attr_accessor :root
  def initialize(nodes)
    self.root = build(nodes.each, :to_i.to_proc)
  end

  def build(nodes, f)
    val = nodes.next rescue nil
    return nil if val.nil? || val == "x"
  
    left = build(nodes, f)
    right = build(nodes, f)
    return Node.new(f.call(val), left, right)
  end

  def print
    def p(node, level)
      if level == 0
        puts("\n")
      elsif node != nil
        p(node.left, level + 1)
        puts(' ' * 4 * level + '->' + node.val)
        p(node.right, level + 1)
      end
    end
    p(self.root, 1)
  end
end
