from polls.models import Job,Person
from polls.serializers import JobSerializer,PersonModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

job = Job(name='Bankier',description = 'liczy pieniadze')
job.save()

person = Person(name='Jan',surrname = 'Kot', sex_type = 1, job = job)
person.save()

serializer = JobSerializer(job)
serializer = PersonModelSerializer(person)
serializer.data
content = JSONRenderer().render(serializer.data)
content

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = PersonModelSerializer(data=data)
deserializer.is_valid()
deserializer.errors
deserializer.fields
deserializer.validated_data
deserializer.save()