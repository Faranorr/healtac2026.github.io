if RUBY_VERSION >= "3.2"
  [NilClass, Object, String, Integer, Float, Array, Hash].each do |klass|
    klass.class_eval do
      def tainted?; false; end
      def untaint; self; end
    end
  end
end
