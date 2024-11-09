require 'pry'
require_relative '../base/node'

class NonBTree
  attr_accessor :root
  def initialize(nodes)
    self.root = build(nodes.each, :to_i.to_proc)
  end

  def build(nodes, f)
    val = nodes.next
    num = nodes.next.to_i
    children = Array.new(num) { build(nodes, f) }
    return NonBNode.new(f.call(val), children)
  end

  def print
    def p(node, level)
      indent = " " * (level * 4)
      puts("#{indent} - #{node.val}")

      node.children.each {|n| p(n, level + 1)}
    end

    p(self.root, 0)
  end

  def ternary_tree_paths
    def dfs(root, path, res)
      if root.children.all? { |c| c.nil? }
        res.append(path.join('->') + '->' + root.val.to_s)
        return 
      end

      root.children.each do | child | 
        if child 
          path.append(root.val)
          dfs(child, path, res)
          path.pop()
        end
      end
    end

    res = []
    dfs(self.root, [], res)
    return res
  end
end