from thermos import app
from thermos import db
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
	db.create_all()
	print('Initialized the database')


@manager.command
def dropdb():
	if prompt_bool("Are you sure you want to loose all your data?"):
		db.drop_all()
		print('Dropped the database')

if __name__ == '__main__':
	manager.run()