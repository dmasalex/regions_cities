from app import app
from flask import render_template, request, redirect, url_for

from forms import PostForm
from app import db
from models import Cities, Regions

from flask_security import login_required


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_region', methods=('POST', 'GET'))
@login_required
def create_region():
    if request.method == 'POST':
        name = request.form['name']
        region = Regions(name=name)

        try:
            db.session.add(region)
            db.session.commit()
            return redirect('/regions')
        except:
            return render_template('regdelete.html')
    else:
        return render_template('create_region.html')


@app.route('/regions')
def getregions():
    regions = Regions.query.all()
    return render_template('regions.html', regions=regions)


@app.route('/reg/<slug>')
def region_detail(slug):
    region = Regions.query.filter(Regions.slug==slug).first()

    city = region.city.all()

    return render_template('region_detail.html', region=region, city=city)


@app.route('/reg/<slug>/update', methods=['POST', 'GET'])
@login_required
def region_update(slug):
    region = Regions.query.filter(Regions.slug==slug).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=region)
        form.populate_obj(region)
        db.session.commit()

        return redirect(url_for('region_detail', slug=region.slug))

    form = PostForm(obj=region)
    return render_template('region_update.html', region=region, form=form)


@app.route('/<slug>/delete')
@login_required
def region_delete(slug):
    region = Regions.query.filter(Regions.slug==slug).first()
    try:
        db.session.delete(region)
        db.session.commit()
        return redirect(url_for('getregions'))
    except:
        return render_template('regdelete.html')


@app.route('/create_city', methods=('POST', 'GET'))
@login_required
def create_city():
    if request.method == 'POST':
        name = request.form['name']
        city = Cities(name=name)

        try:
            db.session.add(city)
            db.session.commit()
            return redirect(url_for('getcities'))
        except:
            return render_template('regdelete.html')
    else:
        return render_template('create_city.html')


@app.route('/cities')
def getcities():
    cities = Cities.query.all()
    return render_template('cities.html', cities=cities)


@app.route('/<slug>')
def city_detail(slug):
    city = Cities.query.filter(Cities.slug==slug).first()

    reg_id = city.region_id
    region = Regions.query.filter(Regions.id == reg_id).first()

    return render_template('city_detail.html', city=city, region=region)


@app.route('/<slug>/update', methods=['POST', 'GET'])
@login_required
def city_update(slug):
    city = Cities.query.filter(Cities.slug == slug).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=city)
        form.populate_obj(city)
        db.session.commit()

        return redirect(url_for('city_detail', slug=city.slug))

    form = PostForm(obj=city)
    return render_template('city_update.html', city=city, form=form)


@app.route('/del/<slug>/delete')
@login_required
def city_delete(slug):
    city = Cities.query.filter(Cities.slug==slug).first()
    try:
        db.session.delete(city)
        db.session.commit()
        return redirect(url_for('getcities'))
    except:
        return render_template('regdelete.html')
