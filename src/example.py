from sample_model import SampleModel

class SampleModelData:
  @staticmethod
  def create(field_name=None, value=None):
    params = dict()
    if field_name is not None:
      params["field_name"] = field_name
    if value is not None:
      params["value"] = value
    
    try:
      data = SampleModel.create(**params)
      return {"result": data, "error": None}
    except Exception as ex:
      print(ex)
      return {"result": None, "error": ex}
  
  @staticmethod
  def get(id):
    try:
      data = SampleModel.get(id=id)
      return {"result": data, "error": None}
    except Exception as ex:
      return {"result": None, "error": ex}


if __name__ == "__main__":
    result = SampleModelData.create(field_name="Test Field", value="Test Value")
    print(result)