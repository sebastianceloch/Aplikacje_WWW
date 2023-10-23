from polls.models import Person, Job
Person.objects.all()
Person.objects.get(id=3)
Person.objects.filter(name__startswith='r')
Job.objects.filter(id__in=Person.objects.values_list('job'))
Job.objects.ordJob.objects.order_by('name')er_by('name')
Person.objects.create(name='Jakub', surrname='Kowalczuk', sex_type=1, job_id=Job.objects.first().id)
