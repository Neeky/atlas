from django.forms import ModelForm
from mysqlbench.models import HostInfo,BenchCase,BenchCaseInstance


class HostInfoForm(ModelForm):
    class Meta(object):
        model=HostInfo
        fields=['name','os','cores','memorys','disks','is_log_ssd','is_data_ssd']

class BenchCaseForm(ModelForm):
    class Meta(object):
        model=BenchCase
        fields=['host_info','mysql_version','variable_name','bench_type','detail']

class BenchCaseInstanceForm(ModelForm):
    class Meta(object):
        model=BenchCaseInstance
        fields=['bench_case','workers','variable_value','truncations_per_seconde','query_per_seconde','duration']




__all__=['HostInfoForm','BenchCaseForm','BenchCaseInstanceForm']