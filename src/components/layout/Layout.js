import MainNavigation from './MainNavigation';
import classes from './Layout.module.css';


//function for the overall layout of the website
function Layout(props) {
  return (
    <div>
      <MainNavigation />
      <main className={classes.main}>{props.children}</main>
    </div>
  );
}

export default Layout;