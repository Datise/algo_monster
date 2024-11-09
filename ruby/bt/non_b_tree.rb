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


class NonBTreeLetters < NonBTree
  attr_accessor :root, :total_nodes
  def initialize(int)
    self.edge_nodes = ('a'..'z').to_a[0..int -1]
    self.total_nodes = @edge_nodes.prepend(nil)
    self.root = build(@total_nodes.each)
  end

  def build(nodes)
    val = nodes.next rescue nil
    return " " if val.nil?
    
    children = @total_nodes.map{|x| val + x}.each { build(nodes) }
    return NonBNode.new(val, children)
  end

  # def dfs(start_index, path)
  #   if is_leaf(start_index)
  #     report(path)
  #     return

  #   get_edges.each do | edge |
  #     path.add(edge)
  #     dfs(start_index + 1, path)
  #     path.pop()
  #   end
  # end

  private 

  def is_leaf(val)
    @total_nodes.include?(val)
  end 

  def get_edges
    @edge_nodes.include?(val)
  end
end 
