require 'minitest/autorun'
require_relative './btree'
class BTreeTest < Minitest::Test
  def test_bfs
    @tree = BTree.new(["3","4","5","x","x","7","x"])
    @tree.print
    result = @tree.levels
    puts result
    assert_equal([[3], [4], [7, 5]], result)
  end
end