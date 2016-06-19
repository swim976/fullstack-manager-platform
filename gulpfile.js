var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    sass = require('gulp-ruby-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    browserify = require('gulp-browserify'),
    jshint = require('gulp-jshint'),
    minifyCss = require('gulp-minify-css'),
    notify = require('gulp-notify');
    // browserSync = require('browser-sync').create();

var DEST = 'dashboard/static';

gulp.task('scripts', function(){
    gulp.src('dashboard/src/js/base.js')
            .pipe(browserify({
                insertGlobals: true,
                debug: !gulp.env.production
            }))
            .pipe(concat('base.js'))        // 这是把上面所有的js文件合并为一个文件
            .pipe(gulp.dest(DEST+'/js'))
            .pipe(rename({suffix: '.min'}))
            .pipe(uglify())
            .pipe(gulp.dest(DEST+'/js'))
            .pipe(notify({
                message: 'Scripts task complete'
            }));
    gulp.src('dashboard/src/js/new.js')
            .pipe(browserify({
                insertGlobals: true,
                debug: !gulp.env.production
            }))
            .pipe(concat('new.js'))        // 这是把上面所有的js文件合并为一个文件
            .pipe(gulp.dest(DEST+'/js'))
            .pipe(rename({suffix: '.min'}))
            .pipe(uglify())
            .pipe(gulp.dest(DEST+'/js'))
            .pipe(notify({
                message: 'Scripts task complete'
            }));
});

gulp.task('concat-css', function(){
    gulp.src([
            'node_modules/gentelella/vendors/bootstrap/dist/css/bootstrap.min.css',
            'node_modules/gentelella/vendors/font-awesome/css/font-awesome.min.css',
        ])
        .pipe(concat('base.min.css'))
        .pipe(minifyCss())
        .pipe(gulp.dest(DEST+'/css'));

    gulp.src(['node_modules/gentelella/build/css/custom.css'])
        .pipe(concat('custom.min.css'))
        .pipe(gulp.dest(DEST+'/css'));

    gulp.src(['node_modules/gentelella/vendors/animate.css/animate.min.css'])
        .pipe(concat('animate.min.css'))
        .pipe(gulp.dest(DEST + '/css'));
});

// gulp.task('default', ['clean'], function(){
//     gulp.start('scripts');
// });

gulp.task('watch', function(){
    gulp.watch('dashboard/src/js/*.js', ['scripts']);
    gulp.watch('dashboard/src/css/*.css', ['concat-css']);
});

gulp.task('default', ['watch']);
