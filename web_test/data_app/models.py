from django.db import models

class Product(models.Model):

    img_path = models.CharField(max_length=255, db_column='图片路径', default="")
    product_code = models.CharField(max_length=765, db_column='货号', default='')
    original_product_code = models.CharField(max_length=765, db_column='原始货号', default='')
    style_code = models.CharField(max_length=765, db_column='款号', default='')
    factory_code = models.CharField(max_length=765, db_column='工厂代码', default='')
    factory_product_code = models.CharField(max_length=765, db_column='工厂货号', default='')
    insole_material = models.CharField(max_length=765, db_column='现管家婆鞋垫材质', default='')
    outsole_material = models.CharField(max_length=765, db_column='现管家婆大底材质', default='')
    lining_material = models.CharField(max_length=765, db_column='现管家婆内里材质', default='')
    upper_material = models.CharField(max_length=765, db_column='现管家婆鞋面材质', default='')
    group = models.CharField(max_length=765, db_column='组别', default='')
    platform = models.CharField(max_length=765, db_column='所属平台', default='')
    cost = models.FloatField(db_column='成本', default=0.0)
    product_name = models.CharField(max_length=765, db_column='品名', default='')
    season_classification = models.CharField(max_length=765, db_column='季节分类', default='')
    season = models.CharField(max_length=765, db_column='季节', default='')
    category = models.CharField(max_length=765, db_column='三级分类', default='')
    first_order_date = models.CharField(max_length=765, db_column='首单日期', default='')
    vip_first_sale_date = models.CharField(max_length=765, db_column='唯品首次售卖时间', default='')
    dew_first_sale_date = models.CharField(max_length=765, db_column='得物首次售卖时间', default='')
    latest_status = models.CharField(max_length=765, db_column='最新上下线状态', default='')
    original_status = models.CharField(max_length=765, db_column='原始货号上线状态', default='')
    
    

    def __str__(self):
        return self.name
