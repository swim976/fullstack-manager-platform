var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    sass = require('gulp-ruby-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    browserify = require('gulp-browserify'),
    jshint = require('gulp-jshint');
    notify = require('gulp-notify');
    // browserSync = require('browser-sync').create();

var DEST = 'dashboard/static';

gulp.task('scripts', function(){
    return gulp.src('dashboard/src/js/*.js')
            .pipe(browserify({
                insertGlobals: true,
                debug: !gulp.env.production
            }))
            .pipe(concat('base.js'))
            .pipe(gulp.dest(DEST+'/js'))
            .pipe(rename({suffix: '.min'}))
            .pipe(uglify())
            .pipe(gulp.dest(DEST+'/js'))
            .pipe(notify({
                message: 'Scripts task complete'
            }));
            // .pipe(browserSync.stream());

    // return gulp.src('dashboard/src/js/*')
    //         .pipe(jshint())
    //         .pipe(jshint.reporter('default'))
    //         .pipe(browserify({
    //             insertGlobals: true,
    //             debug: !gulp.env.production
    //         }))
    //         .pipe(gulp.dest('dashboard/static/js/*'))
    //         .pipe(notify({
    //             message: 'Scripts task complete'
    //         }));
});

gulp.task('clean', function(cb){
    del(['dashboard/ist/js', cb]);
});

// gulp.task('default', ['clean'], function(){
//     gulp.start('scripts');
// });

gulp.task('watch', function(){
    gulp.watch('dashboard/src/js/*.js', ['scripts']);
});

gulp.task('default', ['watch']);
