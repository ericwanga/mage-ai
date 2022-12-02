from mage_ai.data_preparation.variable_manager import get_variable


df = get_variable('example_pipeline', 'load_data', 'output_0')
df.info()