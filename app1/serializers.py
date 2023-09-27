from rest_framework import serializers  
from .models import knowledge_base 
  
class knowledge_base_Serializer(serializers.ModelSerializer):  
     
    class Meta:  
        model = knowledge_base  
        fields = ('__all__')  